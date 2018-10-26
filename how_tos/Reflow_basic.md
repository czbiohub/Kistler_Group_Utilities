# Reflow Basic Tutorial
Reflow is a: [describe]

## Setting up Reflow on your computer
We are downloading reflow from github: click here https://github.com/grailbio/reflow/releases/download/reflow0.6.8/reflow0.6.8.darwin.amd64

On commandline:
```
cd ~/Downloads
chmod ugo+x reflow0.6.8.darwin.amd64
sudo mv reflow0.6.8.darwin.amd64 /usr/local/bin/reflow
```
Now the command `reflow` should output a lot of stuff:
```
   reflow
 The reflow command helps users run Reflow programs, inspect their
 outputs, and query their statuses.

 The command comprises a set of subcommands; the list of supported
 commands can be obtained by running

     reflow -help

 ... (more stuff) ...
```
Then configure reflow, following the [Confluence entry on Reflow (https://czbiohub.atlassian.net/wiki/spaces/DS/pages/838205454/reflow) instructions for configuration:
```
AWS_SDK_LOAD_CONFIG=1 reflow setup-ec2
AWS_SDK_LOAD_CONFIG=1 reflow setup-s3-repository czbiohub-reflow-quickstart-cache
AWS_SDK_LOAD_CONFIG=1 reflow setup-dynamodb-assoc czbiohub-reflow-quickstart
export AWS_REGION=us-west-2
```


## Reflow configuration
It should already be configured to your AWS configurations. Check by `reflow config` to check.
Otherwise, you can configure the `$HOME/.reflow/config.yaml` file to your specifications

# Hello World Example
### Create a file. You can be in any directory.
```
touch hello.rf
```
### Open an editor to write into the file
```
nano hello.rf
```
### Write the following into the file by just `CTRL`+`P`
```
val Main = exec(image := "ubuntu", mem := GiB) (out file) {"
	echo hello world >>{{out}}
"}
```
- Here, Reflow started a new t2.small instance (Reflow matches the workload with available instance types), ran "echo hello world" inside of an Ubuntu container, placed the output in a file, and returned its SHA256 digest. (Reflow represents file contents using their SHA256 digest.)

### The output should look something like this:
```
➜  Desktop reflow  run hello.rf
reflow: run ID: cc7d947d
reflow: total n=1 time=1s
	ident      n   ncache transfer runtime(m) cpu mem(GiB) disk(GiB) tmp(GiB)
	hello.Main 1   1      0B                                         

file(sha256=sha256:a948904f2f0f479b8f8197694b30184b0d2ed1c1cd2a1ec0fb85d299a192a447, size=12)
```

### Reading output
To read the file that was constructed, I can either read it off of the instance OR save it on my computer as another file name.
```
# Reading file from instance
reflow cat a948904f2f0f479b8f8197694b30184b0d2ed1c1cd2a1ec0fb85d299a192a447
#Creating new file on computer that stores the data
reflow cat a948904f2f0f479b8f8197694b30184b0d2ed1c1cd2a1ec0fb85d299a192a447 > helloworld.txt
```
