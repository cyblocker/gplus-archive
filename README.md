# gplus-archive
Generate HTML files to show the archived Google+ Posts.

生成网页文件来展示下载下来的Google+信息流数据。

## Getting Started 开始使用

These instructions will get you download your Google+ stream data and run the script locally to generate your data archive webpage.

这部分说明将会指引如何下载自己的 Google+ 时间线发帖数据，并使用本脚本来生成展示全部发帖数据的单一网页文件。

### Get your data 获取数据
+ Follow instructions on [Google+ Help](https://support.google.com/plus/answer/1045788) to download your data. Make sure to include Google+ Stream Posts data as HTML format.
+ 根据 [Google 账号帮助](https://support.google.com/accounts/answer/3024190?hl=zh-Hans)的说明下载您的数据，请确保下载的数据中包含 Google+ 信息流中的信息数据，并以HTML格式下载。
+ Unzip the takeout file and keep the path to Google+ Stream/Posts folder.
+ 解压缩下载下来的文件，并记录 Google+ Stream/Posts 的文件夹路径。

### Prerequisites 安装运行时环境

_You can find Windows executable binaries in [Release](https://github.com/cyblocker/gplus-archive/releases/latest), and skip to Running part._

_您可以找到适用于 Windows 的可执行文件，请见 [Release](https://github.com/cyblocker/gplus-archive/releases/latest)。您可以跳过下面所有设置步骤，直接运行。_

- [Python 3.x](https://www.python.org/) 
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - The web parser

### Running 运行

Get the archive.py script and run. Or run the binary in [Release](https://github.com/cyblocker/gplus-archive/releases/latest) if using Windows.

获取 archive.py 脚本并运行，运行中需要输入信息流中信息数据的文件夹路径。Windows 用户也可以使用 [Release](https://github.com/cyblocker/gplus-archive/releases/latest) 中的可执行文件。
```
python archive.py
Enter the path of exported Google+ Stream data post folder (Takeout/Google+ Stream/Posts):~/path/to/Takeout/Google+ Stream/Posts
How many posts you want to show on one page? Enter -1 if unlimited: -1
The generated HTML file is saved as ~/path/to/Takeout/Google+ Stream/Posts/archive.html
Upload the file with all image filed under posts folder to serve it online
```

The generated files are archive.html and archive-n.html. Please upload them all with all image files in Posts folder to serve it online.

生成的文件是 archive.html 和 archive-n.html，如果想要网络访问，请将所有archive开头的html文件和图像文件放在同一目录下。

## License 开源许可

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details

## Acknowledgments 致谢

* The release for Windows is created with [PyInstaller](http://www.pyinstaller.org)