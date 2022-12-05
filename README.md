# python based semver
![Alt text](img.png?raw=true "")
#Commmand Line example

## Get Major version
``` shell semVer.py --currentVersion v1.0.0 --versionType major ```
Expected result
``` v2.0.0 ```


## Get Minor version
```shell  semVer.py --currentVersion v1.0.0 --versionType minor ```
Expected result
``` v1.1.0 ```

## Get Hotfix version
``` shell  semVer.py --currentVersion v1.0.0 --versionType hotfix --baseVersion v1.0.0 ```

Expected result
``` v1.0.1 ```