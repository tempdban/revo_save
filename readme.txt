两个存档转换小工具，适用于PC模拟器VBA与K1-SP/K101/K101Plus的sav存档文件格式转换

VBA2K1.exe             将VBA的sav存档文件转换成K1的sav存档文件

K1toVBA.exe            将K1的sav存档文件转换成VBA的sav存档文件


使用方法：

【1】VBA2K1   VBA -> K1
该工具用来将GBA模拟器VBA的存档记忆sav文件转换为 K1-SP/K101/K101plus 的sav文件

用法[1]
在命令行模式下键入下列命令

VBA2K1 xxxx.sav

用法[2]
在窗口模式下直接将VBA的xxxx.sav拖向VBA2K1.exe

生成的K1存档sav文件是 xxxx.gba.sav, 如果GBA ROM文件在K卡上是Zip压缩格式，则要改名为xxxx.zip.sav

注意：

[1] 电脑模拟器的sav文件一定要是VBA的，大小有8K，32K，64K，128K等。

[2] 对于K1-sp和K101，如果GBA ROM文件尺寸大于16MB(不含等于)且ROM在K1固件中登记的, 则不需要转换sav文件，K1直接用
    对于大于16MB且没有K1固件登记的ROM，则需要转换，没有登记的ROM在K1中形成的sav文件也是136K的。由于K1内存的限制
    没有固件登记的ROM不能保证必定能存档或不死机黑屏，但固件登记的就一定能保证。ROM固件登记取决于固件的升级新版本。

    对于K101Plus，由于主板增加了内存，用于GBA ROM的256Mbit(32MB)和用于系统菜单的SDRAM内存是独立的两部分，因此所有
    的K1存档文件都是K1标准的136KB，固件没有登记ROM之说，因而在VBA存档转换时要用这个工具。

【2】K1toVBA   K1 -> VBA

用法：
只能在命令行模式下键入一下命令(因为程序带有参数)

K1toVBA  K1_XXXX.GBA.sav  8

K1toVBA  K1_XXXX.GBA.sav  32

K1toVBA  K1_XXXX.GBA.sav  64

K1toVBA  K1_XXXX.GBA.sav  128

K1toVBA  K1_XXXX.ZIP.sav  8 (32,64,128)

后面的 8,32,64,128 等参数就是GBA ROM的存档大小(实际卡带或VBA模拟器上的存档大小)
转换生成的文件就是 K1_XXX.SAV，将这个文件名改为VBA上玩的ROM一样的前缀名即可。



                                                   周哥(maxzhou88)
