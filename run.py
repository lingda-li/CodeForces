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
      bin_file = os.path.join('./bin', file.replace('.cpp', ''))
      if not os.path.exists(bin_file):
        print("Cannot find", bin_file)
        continue
      in_file = os.path.join(root, file.replace('.cpp', '.in'))
      if not os.path.exists(in_file):
        print("Cannot find", in_file)
        continue
      command = 'perf stat %s < %s' % (bin_file, in_file)
      #command = '%s < %s' % (bin_file, in_file)
      print(command)
      #proc = subprocess.Popen(command, shell=True)
      try:
        subprocess.check_call(command, stderr=subprocess.STDOUT, shell=True)
      except subprocess.CalledProcessError:
        print("Error when running", os.path.join(root, file))
        nerrs += 1
      #break
  #break
print("There were %d errors" % nerrs)
