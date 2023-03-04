**Version 1.0**
--
Youtube to .m4a Downloader
--
- Downloads from YouTube and saves them as .m4a files inside the .exe directory.

- Opens cmd window to function.


## Dependencies
## **[Chocolatey]**
1) Needs to install **[Chocolatey]** (so [FFmpeg] installs easier.)   
or run as admin in powershell:

```shell
$ Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```


## **[FFmpeg]**
2) Needs **[FFmpeg]**
    - or if u installed [Chocolatey] --> open cmd as admin -->
```shell
   $ choco install ffmpeg
```

[Chocolatey]: <https://docs.chocolatey.org/en-us/choco/setup>
[FFmpeg]: <https://www.gyan.dev/ffmpeg/builds/>

