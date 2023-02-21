FROM phusion/baseimage:jammy-1.0.1

ENV DEBIAN_FRONTEND noninteractive

RUN dpkg --add-architecture i386 && \
	apt -y update && \
	apt install -y \
	  libstdc++6:i386 \
	  bsdmainutils \
	  qemu \
	  strace \
	  ltrace \
	  tmux \
	  neovim \
	  gdb \
	  gdb-multiarch \
	  build-essential \
	  git \
	  libffi-dev \
	  libssl-dev \
	  python3 \
	  python3-dev \
	  python3-pip \
	&& rm -rf /var/lib/apt/list/*

RUN apt install -y \
	  openssh-server \
	  netcat \
	&& rm -rf /var/lib/apt/list/*

RUN mkdir -p /var/run/sshd && \
	echo 'root:password' | chpasswd && \
	sed -i 's/\#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
EXPOSE 22
CMD [ "/usr/sbin/sshd", "-D" ]

RUN python3 -m pip install -U pip && \
	python3 -m pip install --no-cache-dir \
	  ipython \
	  angr \
	  pwntools \
	  ropper

RUN git clone --depth 1 https://github.com/pwndbg/pwndbg && \
	cd pwndbg && chmod +x setup.sh && ./setup.sh

WORKDIR /ctf