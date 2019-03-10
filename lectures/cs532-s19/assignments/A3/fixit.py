import subprocess

inlist = list()

with open("results_newcurl.txt") as inf:
    for line in inf:
        inlist.append(line.rstrip("\n"))

        for line in inlist:
            with open("results/text/ggg/" + line) as file:
                content = file.read()
                number = int(line.replace("_result" ,"").replace(".html", "")) + 1141
                with open("results/text/ggg/" + "result" + str(number) + ".html", 'w') as of:
                    of.write(content)

                    # for line in inlist:
                    #    subprocess.run("rm results/text/ggg" + line)
