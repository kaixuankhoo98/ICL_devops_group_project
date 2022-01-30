import subprocess

def pandocConversion(inName, outName, outType = ".pdf", inPath = "default", outPath = "default"):

    args = ["pandoc",]

    if inPath != "default":
        args.append(inPath)

    args.append(inName)
    
    #standalone file and output
    args.append("-s")
    args.append("-o")

    if outPath != "default":
        args.append(outPath + outName + outType)
    else:
        args.append(outName + outType)

    subprocess.Popen(args, shell = True)


#test
#pandocConversion("testInput_00.md", "b")
#pandocConversion("testInput_00.md", "c", outPath= ".\\output\\")