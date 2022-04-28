import os
import sys
import socket
import datetime
import time

import time,threading



def commandsoutput():
    import subprocess   
    subprocess = subprocess.Popen("netstat", shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    print(subprocess_return)
    subprocess_return=str(subprocess_return)
    for line in subprocess_return:
        myfile = open("networkinfo","a")
        myfile.write(line)
        myfile.close()
    print("fin")
commandsoutput()
#********************************************
# glob glob glob it all
# import glob
# import collections

# allFDs = glob.iglob("/proc/*/fd/*")
# inodePidMap = collections.defaultdict(list)

# for fd in allFDs:
#     # split because path looks like: /proc/[pid]/fd/[number]
#     _, _, pid, _, _ = fd.split('/')
#     try:
#         target = os.readlink(fd)
#     except FileNotFoundError:
#         # file vanished, can't do anything else
#         continue

#     # "target" is now something like:
#     #   - socket:[INODE]
#     #   - pipe:[INODE]
#     #   - /dev/pts/N
#     #   - or an actual full file paths
#     if target.startswith("socket"):
#         ostype, inode = target.split(':')
#         # strip brackets from fd string (it looks like: [fd])
#         inode = int(inode[1:-1])
#         inodePidMap[inode].append(int(pid))
        
    
# for inode in inodes:
#     if inode in inodePidMap:
#         for pid in inodePidMap[inode]:
#             try:
#                 with open(f"/proc/{pid}/cmdline", 'r') as cmd:
#                     # /proc command line arguments are delimited by
#                     # null bytes, so undo that here...
#                     cmdline = cmd.read().split('\0')
#                     inodes[inode].append((pid, cmdline))
#             except BaseException:
#                 # files can vanish on us at any time (and that's okay!)
#                 pass
# def populateInodes(name):
#     """ Process IPv4 and IPv6 versions of listeners based on ``name``.

#     ``name`` is either 'udp' or 'tcp' so we parse, for each ``name``:
#          - /proc/net/[name]
#          - /proc/net/[name]6

#     As in:
#          - /proc/net/tcp
#          - /proc/net/tcp6
#          - /proc/net/udp
#          - /proc/net/udp6
#     """

#     isUDP = name == "udp"

#     for ver in ["", "6"]:
#         with open(f"/proc/net/{name}{ver}", 'r') as proto:
#             proto = proto.read().splitlines()
#             proto = proto[1:]  # drop header row

#             for cxn in proto:
#                 cxn = cxn.split()

#                 # /proc/net/udp{,6} uses different constants for LISTENING
#                 if isUDP:
#                     # These constants are based on enum offsets inside
#                     # the Linux kernel itself. They aren't likely to ever
#                     # change since they are hardcoded in utilities.
#                     isListening = cxn[3] == "07"
#                 else:
#                    isListening = cxn[3] == "0A"

#                # Right now this is a single-purpose tool so if process is
#                # not listening, we avoid further processing of this row.
#                 if not isListening:
#                     continue

#                 ip, port = cxn[1].split(':')
#                 if ver:
#                    ip = ipv6(ip)
#                 else:
#                    ip = ipv4(ip)

#                 port = int(port, 16)
#                 inode = cxn[9]

#                # We just use a list here because creating a new sub-dict
#                # for each entry was noticeably slower than just indexing
#                # into lists.
#                 inodes[int(inode)] = [ip, port, f"{name}{ver}"]


# populateInodes("tcp")
# populateInodes("udp")
# def ipv6(addr):
#     """ Convert /proc IPv6 hex address into standard IPv6 notation. """
#     # turn ASCII hex address into binary
#     addr = codecs.decode(addr, "hex")

#     # unpack into 4 32-bit integers in big endian / network byte order
#     addr = struct.unpack('!LLLL', addr)

#     # re-pack as 4 32-bit integers in system native byte order
#     addr = struct.pack('@IIII', *addr)

#     # now we can use standard network APIs to format the address
#     addr = socket.inet_ntop(socket.AF_INET6, addr)
#     return addr

# def ipv4(addr):
#     """ Convert /proc IPv4 hex address into standard IPv4 notation. """
#     # Instead of codecs.decode(), we can just convert a 4 byte hex
#     # string to an integer directly using python radix conversion.
#     # Basically, int(addr, 16) EQUALS:
#     # aOrig = addr
#     # addr = codecs.decode(addr, "hex")
#     # addr = struct.unpack(">L", addr)
#     # assert(addr == (int(aOrig, 16),))
#     addr = int(addr, 16)

#     # system native byte order, 4-byte integer
#     addr = struct.pack("=L", addr)
#     addr = socket.inet_ntop(socket.AF_INET, addr)
#     return addr