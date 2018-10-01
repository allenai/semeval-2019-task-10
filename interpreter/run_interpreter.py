import argparse
import subprocess
import os
import json

dockerImg = "allenai/semeval-2019-task-10:1.0"
batchSize = 10

def getDirName(path):
    return (os.path.dirname(os.path.realpath(path)), os.path.basename(path))

def safeRemove(path):
    if os.path.exists(path):
        os.remove(path)

def main(inputFile, outputFile):

    with open(inputFile) as f:
        programs = json.load(f)
    remainingPrograms = list(programs)

    tmpInputFile = inputFile + ".tmp"
    (tmpInputDir, tmpInputName) = getDirName(tmpInputFile)

    tmpOutputFile = outputFile + ".tmp"
    (tmpOutputDir, tmpOutputName) = getDirName(tmpOutputFile)

    responses = []
    with open(tmpOutputFile, 'w') as output:
        json.dump(responses, output)

    # Pull the docker image
    pullCmd = r"""docker pull {0}""".format(dockerImg)
    subprocess.call(pullCmd, shell=True)

    batch = 1
    while remainingPrograms:
        currentBatchSize = min(len(remainingPrograms), batchSize)
        print("Batch {} - Solving {} of the remaining {} program(s)".format(
            batch,
            currentBatchSize,
            len(remainingPrograms))
        )
        nextProgram = remainingPrograms[0]

        # Create a temporary file with the programs for this batch
        batchPrograms = remainingPrograms[:currentBatchSize]
        with open(tmpInputFile, 'w') as output:
            json.dump(batchPrograms, output)

        # Run the docker image
        dockerInputMnt = "/mnt_input"
        dockerOutputMnt = "/mnt_output"
        runCmd = r"""docker run -v {2}:{1} -v {5}:{4} {0} "org.allenai.euclid.LfInterpreter {1}/{3} {4}/{6}" """.format(
            dockerImg,
            dockerInputMnt,
            tmpInputDir,
            tmpInputName,
            dockerOutputMnt,
            tmpOutputDir,
            tmpOutputName
        )
        subprocess.call(runCmd, shell=True)

        # Gather the responses for that batch and remove the corresponding programs from the list of remaining programs
        with open(tmpOutputFile) as f:
            newResponses = json.load(f)

        # If there is no response for the 1st program, augment the list of responses with a NoResponse for that program
        if not filter(lambda x: x["id"] != nextProgram["id"], newResponses):
            nextProgramResponse = {"id": nextProgram["id"], "response": "NoResponse"}
            newResponses.append(nextProgramResponse)

        # Remove the programs corresponding to the responses from the list of remaining programs
        for r in newResponses:
            remainingPrograms = list(filter(lambda x: x["id"] != r["id"], remainingPrograms))

        # Update the list of responses
        responses = responses + newResponses
        batch = batch + 1

    with open(outputFile, 'w') as output:
        json.dump(responses, output, indent=4)

    safeRemove(tmpInputFile)
    safeRemove(tmpOutputFile)

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input",
                        type=str,
                        help="Input json file containing the program ids and their logical form.")
    parser.add_argument("output",
                        type=str,
                        help="Output json file with the program ids and the corresponding interpreter response.")
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        raise Exception("The input argument should be a path to an existing file.")
    if os.path.isdir(args.output):
        raise Exception("The output argument should be a path to a file, not a directory.")

    main(args.input, args.output)
