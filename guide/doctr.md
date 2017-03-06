# Deploying documentation on GhPages


## Installing doctr locally

    $ pip install doctr
    Collecting doctr
    Requirement already satisfied: requests in /Users/bussonniermatthias/anaconda/lib/python3.6/site-packages (from doctr)
    Requirement already satisfied: cryptography in /Users/bussonniermatthias/anaconda/lib/python3.6/site-packages (from doctr)
    Requirement already satisfied: idna>=2.0 in /Users/bussonniermatthias/anaconda/lib/python3.6/site-packages (from cryptography->doctr)
    Requirement already satisfied: pyasn1>=0.1.8 in /Users/bussonniermatthias/anaconda/lib/python3.6/site-packages (from cryptography->doctr)
    Requirement already satisfied: six>=1.4.1 in /Users/bussonniermatthias/anaconda/lib/python3.6/site-packages (from cryptography->doctr)
    Requirement already satisfied: setuptools>=11.3 in /Users/bussonniermatthias/anaconda/lib/python3.6/site-packages (from cryptography->doctr)
    Requirement already satisfied: cffi>=1.4.1 in /Users/bussonniermatthias/anaconda/lib/python3.6/site-packages (from cryptography->doctr)
    Requirement already satisfied: pycparser in /Users/bussonniermatthias/anaconda/lib/python3.6/site-packages (from cffi>=1.4.1->cryptography->doctr)
    Installing collected packages: doctr
    Successfully installed doctr-1.4.1

## enabling Travis

Go to `https://travis-ci.org/profile/<Your username>` and enable your repository

or use the `$ travis enable command`

## Setting up the repo

Simply run `doctr configure` in the repository



    ~/dev/zero_to_docs master "!!" $ doctr configure
    What is your GitHub username? Carreau
    Enter the GitHub password for Carreau: <nysecretpassord>
    A two-factor authentication code is required: app
    Authentication code: <my 2fA AUTH CODE>
    What repo do you want to build the docs for (org/reponame, like 'drdoctr/doctr')? Carreau/zero_to_docs
    What repo do you want to deploy the docs to? [Carreau/zero_to_docs]


The rest is just output:

    Generating public/private rsa key pair.
    Your identification has been saved in github_deploy_key.
    Your public key has been saved in github_deploy_key.pub.
    The key fingerprint is:
    2f:d9:4f:eb:16:42:3e:cf:14:e5:7d:79:aa:6e:45:84 doctr deploy key for Carreau/zero_to_docs
    The key's randomart image is:
    +--[ RSA 4096]----+
    |             .   |
    |            E o  |
    |             + ..|
    |          . . o.+|
    |        So   o .o|
    |         ++ o o  |
    |        o o*.+   |
    |         . o*.   |
    |           ==    |
    +-----------------+

    The deploy key has been added for Carreau/zero_to_docs.

    You can go to https://github.com/Carreau/zero_to_docs/settings/keys to revoke the deploy key.

    ================== You should now do the following ==================

    1. Commit the file github_deploy_key.enc.

    2. Add

        script:
        - set -e
        - # Command to build your docs
        - pip install doctr
        - doctr deploy

    to the docs build of your .travis.yml.  The 'set -e' prevents doctr from
    running when the docs build fails. Use the 'script' section so that if
    doctr fails it causes the build to fail.

    3. Put

        env:
        global:
            - secure: "rCA/1nkkhaGAhicPXGzokoKxODEWBC6GVTOQxkhZKBPXVy33va2MoBr0U7ZcZ8v0bTRMitTRO5tfRv+liS5TC6auynPEnArGtZAmjm5PMn6kMD02Wtz9We63zTWha5i+viCSIa2UUaE/K9comAK6ZbVY98C3yAPeB3/2+cI4r0nApVxXM5qcdcuclV7gHeYmOxHItnFMz/yftIfbv79BOh32OHUFBU7oDuPM6CE7rWnz3Ol5fgdPQW52M803S8r5DtA53Cw1E8GnD3RLSyLPdz7BnEKHzapPEfmOD9Ey19zQljVLYJ2Kot5Cg8CTPj8cfhy0CaYQSJLuNc2v8vyg2W1/x+eZ4AlfwhiOiYNPowpqfvHt18HJ5aTCWlUIjhkRY96qAf82uC16OzWIY87aLcJmPi9jYKpv+JKXaIqOKsUj4jFpscffcnXdKBShWOxLpTpaNsiBSijpoiUdlLCgBbqAwr0YtyCH/F61TNzC6OlHeO7kiJ+fI98XpEX91DerpLPsm5pjGSmrovg8PFJGP+FVnouxBwhW51Whuwc49Jyr8hnHHz25x7No12Y/+UUiVCh1XDYelwVzgCwWdTH6ZMOfjkirdT2K19Hhusw6fyhxY9O8ej2Lw/uLQbmU7IW3ONbOUEwQHRJUSfyevM9aoI4HwdsKlDbvB5s0vswzDg0="

    in your .travis.yml.


Follow above instruction, commit and push,  the docs should be deployed as
`https://<username>.github.io/<project_name>/docs/`

A working example can be found in git history if it can be of help.
