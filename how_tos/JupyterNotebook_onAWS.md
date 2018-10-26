# Running Jupyter Notebook on AWS

## Launching an instance with anaconda built in

```
aegea launch --iam-role S3fromEC2 --ami-tags Name=czbiohub-cupcakes -t t2.micro --duration-hours 1  <instance name>

aegea ssh ubuntu@<instance name>
```

## Keep instance running even if connection is lost
This will keep Jupyter notebook running forever even if your network connection breaks

Do one of:

`screen`
<br></br> --- OR if you know tmux much better ---

`tmux`

## Launch jupyter notebook in screen

```
jupyter notebook
```

ouput should look like this:
```
ubuntu@kalani-35:~$ jupyter notebook
[I 00:54:22.380 NotebookApp] Writing notebook server cookie secret to /run/user/1000/jupyter/notebook_cookie_secret
[I 00:54:25.207 NotebookApp] Serving notebooks from local directory: /home/ubuntu
[I 00:54:25.207 NotebookApp] The Jupyter Notebook is running at:
[I 00:54:25.208 NotebookApp] http://localhost:8888/?token=992ca4662c792f2c449ddf0113801769ceb892fbe3c60884
[I 00:54:25.208 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 00:54:25.208 NotebookApp] No web browser found: could not locate runnable browser.
[C 00:54:25.209 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=992ca4662c792f2c449ddf0113801769ceb892fbe3c60884
```

## Bind Jupyter Notebook Port to Port 8899
By default, Jupyter Notebook uses port 8888, and if you have other Jupyter Notebooks running locally, this causes conflict. By rebinding the port to 8899, then we can have Jupyter Notebooks running both locally and on AWS.

This is the command that binds the remote port 8888 to your local port 8899. **On a terminal  linked to your computer.**

```
aegea ssh ubuntu@kalani-35 -NL localhost:8899:localhost:8888
```

Go to http://localhost:8899 on your laptop
enter token at the end of
in my case token= `992ca4662c792f2c449ddf0113801769ceb892fbe3c60884`


Now you can run jupyter using an instance!!!

# Terminate or stop Instance
Remember to terminate or stop your instance by going onto console.
