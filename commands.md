# Pycom Commands

## Check device location
```
python3 -m there detect 
```

## Connect to device
```
python3 -m there -i
```

## Push files to device
Single file:
```
python3 -m there push main.py /flash
```

Multiple files:
```
python3 -m there push *.py /flash
```

## Push lib files
Lib files can be found at GitHub: [link](https://github.com/pycom/pycom-libraries)
```
python3 -m there push *.py /lib
```

## Soft Reset Device
soft reset restarts device, and executes the `/flash/main.py` file.
Soft reset is done by pressing `ctrl + d` 

## Other
List files in flash folder:
```
python3 -m there ls -l /flash/*
```

Display content of main.py:
```
python3 -m there cat /flash/main.py
```