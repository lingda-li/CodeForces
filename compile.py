import os
import subprocess

# traverse whole directory
nerrs = 0
for root, dirs, files in os.walk(r'.'):
  # select file name
  for file in files:
    # check the extension of files
    if file.endswith('.cpp'):
      # print whole path of files
      #print(os.path.join(root, file))
      command = 'g++ -O3 -static %s -o bin/%s' % (os.path.join(root, file), file.replace('.cpp', ''))
      print(command)
      #proc = subprocess.Popen(command, shell=True)
      #proc.wait()
      try:
        subprocess.check_call(command, shell=True)
      except subprocess.CalledProcessError:
        print("Error when compiling", os.path.join(root, file))
        nerrs += 1
      #break
  #break
print("There were %d errors" % nerrs)
