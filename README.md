# 2020-HMI-ISP-8
课题名称：基于表情识别的智能家居控制

关键词：表情识别，情绪捕捉，智能家居

参考文献：





环境的安装建议使用anaconda：

conda create -n FER python=3.6

source activate FER

conda install cudatoolkit=10.1

conda install cudnn=7.6.5

pip install -r requirements.txt


文件夹需要如下放置：

D:\git_projects\hiv_image\08         由于使用了绝对路径

由于github上传限制，文件音乐和视频上传到谷歌网盘，连接如下：用于替换08下的music文件夹：

https://drive.google.com/file/d/1nuDbHIEjsh8uYmMIQ6FgCJhugjlGHQad/view?usp=sharing



运行代码则需要

conda activate FER

然后在08/2的目录下：

python recognition_camera.py





Reference:

1.基于表情识别和情绪感知的智能家居 

2.关键词：表情识别、神经网络训练、人脸识别定位 

3.参考文献：[1]张志勰,虞旦. BP和RBF神经网络在函数逼近上的对比与研究[J]. 工业控制计算机,2018,31(05):119-120.

[2]张翠平，苏光大．人脸识别技术综述[J]．中国图像图形学报, XX，5(11): 885894

[3]金忠,胡钟山,等．基于BP 神经网络的人脸识别方法[J. Journal of ComputerResearch&Development , 1999 ,36(3): 274277

[4]蒋宗礼. 人工神经网络导论[M]．北京:高等教育出版社, XX

