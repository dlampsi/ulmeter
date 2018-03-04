FROM centos:centos7
MAINTAINER dlampsi@gmail.com

RUN yum install -y rpm-build rpmdevtools git tree
RUN rpmdev-setuptree

ADD SPECS /root/rpmbuild/SPECS
COPY SOURCES /root/rpmbuild/SOURCES
# RUN cd /root/rpmbuild \
#     && rpmbuild -ba SPECS/ulmeter.spec
# RUN tree /root/rpmbuild/

CMD rpmbuild -ba /root/rpmbuild/SPECS/ulmeter.spec
