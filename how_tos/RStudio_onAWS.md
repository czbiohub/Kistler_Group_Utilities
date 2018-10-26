# Running R Studio on AWS

## Launching an instance with R-Studio built in
```
aegea launch --ami ami-bca063c4 --instance-type t2.micro --iam-role S3fromEC2 --security-groups='R/RStudio Server and JupyterHub' --duration-hours 1 <instance name>

aegea ssh ubuntu@<instance name>
```
- ID of us-west-2 (Oregon) AMI from http://www.louisaslett.com/RStudio_AMI/
- Authorize yourself to copy files from EC2: --iam-role S3fromEC2
- Instance type from https://ec2instances.info/

## Get Public DNS for RStudio server access
```
curl -s http://169.254.169.254/latest/meta-data/public-hostname
```
- should look like: `ec2-54-245-197-34.us-west-2.compute.amazonaws.com`

## Enter Public DNS into browser (the entire Public DNS output)
- login menu will pop-up
  - username: `rstudio`
  - password: `rstudio`

# Pushing Data to RStudio
On your local machine, should be able to do this. HOWEVER, for some reason the set-up doesn't allow for this. Have to currently manually upload from the web-interface.
```
scp -i /path/to/keyPair/myFile.pem /path/to/local/file ubuntu@<PublicDNS>:/home/rstudio
#.pem file is usually within ~/.ssh/<file.pem>
```

# Pull Down your data
While you are on your local terminal.
To copy a single file:
```
scp -i ~/.ssh/<file.pem> ubuntu@<PublicDNS>:~/path/to/dir/on/Virtual_Machine /destination/on/local

#~/path/to/dir/on/Virtual_Machine will most likeley start with /home/rstudio/<file_name>
```
Or an entire directory:
```
scp -i ~/.ssh/<file.pem> -r ubuntu@<PublicDNS>:~/path/to/dir/on/Virtual_Machine /destination/on/local
```

# Terminate or stop Instance
Go onto console and terminate or stop instance
