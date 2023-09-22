import argparse
import os
import subprocess


parser = argparse.ArgumentParser(description='Run benchmarks')
parser.add_argument('--mem', '-m', action='store_true', default=False)
parser.add_argument('--repeat', '-r', type=int, default=1)
args = parser.parse_args()

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
      if args.mem:
        in_file = os.path.join(root, file.replace('.cpp', '.min'))
      else:
        in_file = os.path.join(root, file.replace('.cpp', '.in'))
      if not os.path.exists(in_file):
        print("Cannot find", in_file)
        continue
      command = 'perf stat -e cycles,cycles:u,instructions:u,cache-misses:u,cache-references:u,stalled-cycles-backend:u,stalled-cycles-frontend:u,dTLB-load-misses:u '
      if args.repeat > 1:
        command += '-r %d ' % args.repeat
        perl_command = "perl -0777pe '$_=$_ x %d' %s > tmp" % (args.repeat, in_file)
        try:
          subprocess.check_call(perl_command, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError:
          print("Error when repeating", os.path.join(root, in_file))
          nerrs += 1
          continue
        in_file = 'tmp'
      command += '%s < %s' % (bin_file, in_file)
      print(command)
      try:
        #proc = subprocess.Popen(command, shell=True)
        subprocess.check_call(command, stderr=subprocess.STDOUT, shell=True)
      except subprocess.CalledProcessError:
        print("Error when running", os.path.join(root, file))
        nerrs += 1
      #break
  #break
print("There were %d errors" % nerrs)
