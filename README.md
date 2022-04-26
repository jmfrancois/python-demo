# Talend Python demo package

## How to get python

Please install and use [asdf](https://asdf-vm.com). Once installed it will use the `.tool-versions` file to be aligned with your poject python supported version.

    asdf install python 3.10.4
    asdf reshim python
    pip install zc.buildout

## What is buildout

zc.buildout is a installation CLI which take a configuration file `buildout.cfg` by default and execute the parts recipe one by one.

On the file system we have :

- setup.py define metadata about the package and so requirements
- talend/**init**.py define namespace (look at the file)
- talend/demo/**init**.py is your code
- buildout.cfg define the installation process (kind of makefile)

Then you have the following folders and files created:

- bin/buildout
- parts
- develop-eggs

So you can execute the installation process:

    bin/buildout

Now we have our super `py` command which is a python loaded with our package !

    bin/py

```python
>>> import talend.demo
hello
```
