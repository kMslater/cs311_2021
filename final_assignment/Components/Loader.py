import sys
import time
import itertools

# Method shows a loading animation.
# Receives an input for the loading text.
def loadingAnimation(loadingText):

    # Loading Animation Sequence.
    loadingCharacters = ['[#       ]', '[##      ]',
                         '[###     ]', '[####    ]',
                         '[#####   ]', '[######  ]',
                         '[####### ]', '[########]']

    loadCount = 0

    # Loop through each animation sequence.
    for animationCharacters in itertools.cycle(loadingCharacters):

        if loadCount == 8:
            break

        sys.stdout.write('\r        ' + loadingText +
                         ': ' + animationCharacters)
        sys.stdout.flush()
        time.sleep(0.3)
        loadCount += 1

    sys.stdout.write('\r       Success! \n\n\n')