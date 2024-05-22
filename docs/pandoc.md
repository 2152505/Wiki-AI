### 信息查看

可以通过以下命令来观察相关的信息 1.查看程序支持的输入文件格式：

`pandoc --list-input-formats`
查看程序支持代码高亮的编程语言：<br/>

`pandoc --list-highlight-languages`
查看程序帮助：<br/>

`pandoc --help`
常用命令<br/>
Pandoc 支持多种命令，以下是一些常用的命令。<br/>

1. 转换 Markdown 为 HTML<br/>
   `pandoc -s input.md -o output.html`<br/>
   其中“-s input.md”表示将 Markdown 文件转换为 HTML 文件，“-o output.html”表示将结果输出到 output.html 文件中。<br/>

2. 转换 Markdown 为 PDF<br/>
   `pandoc -s input.md -o output.pdf`<br/>
   和将 Markdown 转换为 HTML 的命令类似，只是输出的文件类型不同，需要使用 PDF。<br/>

3. 转换多个文件<br/>
   `pandoc -s file1.md file2.md -o output.html`<br/>
   可以同时将多个 Markdown 文件转换为同一个格式的文件。<br/>

4. 引入 CSS 样式<br/>
   `pandoc -s input.md -o output.html --css=mycss.css`<br/>
   可以使用--css 选项引入自定义的 CSS 样式。<br/>

5. 生成目录<br/>
   `pandoc -s input.md -o output.html --toc`<br/>
   可以在生成的 HTML 文件中自动生成目录。<br/>

6. 转换为其他格式<br/>
   `pandoc -s input.md -o output.docx`<br/>
   除了将 Markdown 转换为 HTML 或 PDF，还可以将其转换为 Word 等其他格式<br/>

实际操作<br/>
桌面上放了我需要转换的 word 文档，（注意需要保存为 docx），利用如下命令来实现格式转化。<br/>

`pandoc -s input.docx -t markdown -o output.md`<br/>
第一次报错，找不到目标文件或目录，此时我认为是路径问题，用 cd Desktop 进入桌面，再次尝试还是报错，还是找不到目标文件。这时候没什么办法，只能继续在网上找教程，发现 @Curious zixi 老师给出的提示：文件名中不能包含空格 ，发现自己给文件命名时经常习惯性用空格来隔断字符，结果导致命令无法被识别。于是尝试修改文件名，改为：现西 3 笔记，然后成功在桌面成 md 文件。（Pandoc 软件运行时默认的文件地址和命令行中的路径是一致的）
