
# (Anssi 02/2008) osp Disabled by Fedora and Debian:
# (misc 02/2010) oracle, need library not in distro
%define	EXCLUDE_MODULES	osp db_oracle

Summary:	SIP Server
Name:		opensips
Version:	1.6.2
Release:	%mkrel 3
License:	GPLv2+
Group:		System/Servers
Source0:	http://www.opensips.org/pub/%{name}/%{version}/src/%{name}-%{version}-tls_src.tar.gz
# not sent upstream yet
Patch0:     opensips-1.6.2-fix_format_string.diff

URL:		http://www.opensips.org/

BuildRequires:	expat-devel
BuildRequires:	libxml2-devel
BuildRequires: 	bison
BuildRequires: 	flex
# needed by snmpstats
BuildRequires:	radiusclient-ng-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel

# required by snmpstats module
BuildRequires:	lm_sensors-devel
BuildRequires:	net-snmp-devel
BuildRequires:	unixODBC-devel
BuildRequires:	openssl-devel
BuildRequires:	expat-devel
BuildRequires:	xmlrpc-c-devel
BuildRequires:	confuse-devel
BuildRequires:	db4-devel
BuildRequires:	openldap-devel
BuildRequires:	curl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
# for xsubpp:
BuildRequires:	perl-devel
BuildRequires:  json-c-devel
# do not use memcached-devel
# https://qa.mandriva.com/show_bug.cgi?id=58287
BuildRequires:  pkgconfig(libmemcached)
BuildRequires:  GeoIP-devel
BuildRequires:  pkgconfig(libpcre)  

# (Anssi 02/2008) Suggests as per debian:
Suggests: %{name}-acc_radius
Suggests: %{name}-auth_diameter
#Suggests: %{name}-avp_radius
Suggests: %{name}-carrierroute
Suggests: %{name}-cpl-c
Suggests: %{name}-group_radius
Suggests: %{name}-db_berkeley
Suggests: %{name}-h350
Suggests: %{name}-jabber
Suggests: %{name}-ldap
Suggests: %{name}-db_mysql
Suggests: %{name}-perl
Suggests: %{name}-perlvdb
Suggests: %{name}-db_postgres
Suggests: %{name}-presence
Suggests: %{name}-presence_mwi
Suggests: %{name}-presence_xml
Suggests: %{name}-pua
Suggests: %{name}-pua_bla
Suggests: %{name}-pua_mi
Suggests: %{name}-pua_usrloc
Suggests: %{name}-pua_xmpp
Suggests: %{name}-rls
Suggests: %{name}-seas
Suggests: %{name}-sms
Suggests: %{name}-snmpstats
Suggests: %{name}-tlsops
Suggests: %{name}-db_unixodbc
#Suggests: %{name}-uri_radius
Suggests: %{name}-xcap_client
Suggests: %{name}-xmpp

Obsoletes: openser < 1.6.0
Requires(post):	rpm-helper
Requires(preun):rpm-helper
Requires(preun):rpm-helper
BuildRoot: 	%{_tmppath}/%{name}-root

%description
OpenSIPS is a very fast and flexible SIP (RFC3261)
proxy server. Written entirely in C, opensips can handle thousands calls
per second even on low-budget hardware. A C Shell like scripting language
provides full control over the server's behaviour. It's modular
architecture allows only required functionality to be loaded.
Currently the following modules are available: digest authentication,
CPL scripts, instant messaging, MySQL and UNIXODBC support, a presence agent,
radius authentication, record routing, an SMS gateway, a jabber gateway, a
transaction and dialog module, statistics support,
registrar and user location.

%package	acc_radius
Summary:	Accounts transactions information with radius support
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-acc_radius < 1.6.0

%description	acc_radius
ACC module is used to account transactions information to different backends
like syslog, SQL, RADIUS, DIAMETER.

%package	auth_diameter
Summary:	Performs authentication using a Diameter server
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-diameter < 1.6.0

%description	auth_diameter
This module implements SIP authentication and authorization with DIAMETER
server, namely DIameter Server Client (DISC).

%package	auth_aaa
Summary:	Performs authentication using a Radius server
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	auth_aaa
This module implements SIP authentication and authorization with RADIUS
server, using AAA.

%package	carrierroute
Summary:	Routing extension suitable for carriers
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-carrierroute < 1.6.0

%description	carrierroute
A module which provides routing, balancing and blacklisting capabilities.

%package	cpl-c
Summary:	Call Processing Language interpreter
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-cpl-c < 1.6.0

%description	cpl-c
This module implements a CPL (Call Processing Language) interpreter.
Support for uploading/downloading/removing scripts via SIP REGISTER method
is present.

%package	db_berkeley
Summary:	Berkley DB backend support
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-db_berkeley < 1.6.0

%description	db_berkeley
This is a module which integrates the Berkeley DB into OpenSIPS. It implements
the DB API defined in OpenSIPS.

%package	h350
Summary:	H350 implementation	
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-h350 < 1.6.0

%description	h350
The OpenSIPS H350 module enables an OpenSIPS SIP proxy server to access SIP
account data stored in an LDAP [RFC4510] directory  containing H.350 [H.350]
commObjects.

%package	jabber
Summary:	Gateway between OpenSIPS and a jabber server
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-jabber < 1.6.0

%description 	jabber
Jabber module that integrates XODE XML parser for parsing Jabber messages.

%package	ldap
Summary:	LDAP connector
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-ldap < 1.6.0

%description	ldap
The LDAP module implements an LDAP search interface for OpenSIPS.

%package	db_mysql
Summary:	MySQL Storage Support for the OpenSIPS
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-mysql < 1.6.0

%description 	db_mysql
The %{name}-db_mysql package contains the MySQL plugin for %{name}, which allows
a MySQL-Database to be used for persistent storage.

%package 	perl
Summary:	Helps implement your own OpenSIPS extensions in Perl
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-perl < 1.6.0

%description	perl
The time needed when writing a new OpenSIPS module unfortunately is quite
high, while the options provided by the configuration file are limited to
the features implemented in the modules. With this Perl module, you can
easily implement your own OpenSIPS extensions in Perl.  This allows for
simple access to the full world of CPAN modules. SIP URI rewriting could be
implemented based on regular expressions; accessing arbitrary data backends,
e.g. LDAP or Berkeley DB files, is now extremely simple.

%package	perlvdb
Summary:	Perl virtual database engine
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-perl
Obsoletes:	openser-perlvdb < 1.6.0

%description	perlvdb
The Perl Virtual Database (VDB) provides a virtualization framework for
OpenSIPS's database access. It does not handle a particular database engine
itself but lets the user relay database requests to arbitrary Perl functions.

%package	db_postgres
Summary:	PostgreSQL Storage Support for the OpenSIPS
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-db_postgres < 1.6.0

%description	db_postgres
The %{name}-db_postgres package contains the PostgreSQL plugin for %{name},
which allows a PostgreSQL-Database to be used for persistent storage.

%package	presence
Summary:	Presence server
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-presence < 1.6.0

%description	presence
This module implements a presence server. It handles PUBLISH and SUBSCRIBE
messages and generates NOTIFY messages. It offers support for aggregation
of published presence information for the same presentity using more devices.
It can also filter the information provided to watchers according to privacy
rules.

%package	presence_mwi
Summary:	Extension to Presence server for Message Waiting Indication
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-presence
Obsoletes:	openser-presence_mwi < 1.6.0

%description	presence_mwi
The module does specific handling for notify-subscribe message-summary
(message waiting indication) events as specified in RFC 3842. It is used
with the general event handling module, presence. It constructs and adds
message-summary event to it.

%package	presence_xml
Summary:	SIMPLE Presence extension
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-presence
Requires:	%{name}-xcap_client
Obsoletes:	openser-presence_xml < 1.6.0

%description	presence_xml
The module does specific handling for notify-subscribe events using xml bodies.
It is used with the general event handling module, presence.

%package	pua
Summary:	Offer the functionality of a presence user agent client
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-pua < 1.6.0

%description	pua
This module offer the functionality of a presence user agent client, sending
Subscribe and Publish messages.

%package	pua_bla
Summary:	BLA extension for PUA
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-pua
Requires:	%{name}-presence
Obsoletes:	openser-pua_bla < 1.6.0

%description	pua_bla
The pua_bla module enables Bridged Line Appearances support according to the
specifications in draft-anil-sipping-bla-03.txt.

%package	pua_mi
Summary:	Connector between usrloc and MI interface
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-pua
Obsoletes:	openser-pua_mi < 1.6.0

%description	pua_mi
The pua_mi sends offer the possibility to publish presence information
via MI transports.  Using this module you can create independent
applications/scripts to publish not sip-related information (e.g., system
resources like CPU-usage, memory, number of active subscribers ...)

%package	pua_usrloc
Summary:	Connector between usrloc and pua modules
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-pua
Obsoletes:	openser-pua_usrloc < 1.6.0

%description	pua_usrloc
This module is the connector between usrloc and pua modules. It creates the
environment to send PUBLISH requests for user location records, on specific
events (e.g., when new record is added in usrloc, a PUBLISH with status open
(online) is issued; when expires, it sends closed (offline)). Using this
module, phones which have no support for presence can be seen as
online/offline.

%package	pua_xmpp
Summary:	SIMPLE-XMPP Presence gateway
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-pua
Requires:	%{name}-presence
Requires:	%{name}-xmpp
Obsoletes:	openser-pua_xmpp < 1.6.0

%description	pua_xmpp
This module is a gateway for presence between SIP and XMPP. It translates one
format into another and uses xmpp, pua and presence modules to manage the
transmition of presence state information.

%package	rls
Summary:	Resource List Server
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-pua
Requires:	%{name}-presence
Obsoletes:	openser-rls < 1.6.0

%description	rls
The modules is a Resource List Server implementation following the
specification in RFC 4662 and RFC 4826.

%package	seas
Summary:	Transfers the execution logic control to a given external entity
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-seas < 1.6.0

%description	seas
SEAS module enables OpenSIPS to transfer the execution logic control of a sip
message to a given external entity, called the Application Server. When the
OpenSIPS script is being executed on an incoming SIP message, invocation of
the as_relay_t() function makes this module send the message along with some
transaction information to the specified Application Server. The Application
Server then executes some call-control logic code, and tells OpenSIPS to take
some actions, ie. forward the message downstream, or respond to the message
with a SIP repy, etc

%package	sms
Summary:	Gateway between SIP and GSM networks via sms
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-sms < 1.6.0

%description	sms
This module provides a way of communication between SIP network (via SIP
MESSAGE) and GSM networks (via ShortMessageService). Communication is
possible from SIP to SMS and vice versa.  The module provides facilities
like SMS confirmation--the gateway can confirm to the SIP user if his
message really reached its destination as a SMS--or multi-part messages--if
a SIP messages is too log it will be split and sent as multiple SMS.

%package	snmpstats
Summary:	SNMP management interface for the OpenSIPS
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-snmpstats < 1.6.0

%description	snmpstats
The %{name}-snmpstats package provides an SNMP management interface to
OpenSIPS.  Specifically, it provides general SNMP queryable scalar statistics,
table representations of more complicated data such as user and contact
information, and alarm monitoring capabilities.

%package	tlsops
Summary:	TLS-relating functions for the OpenSIPS
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-tlsops < 1.6.0

%description	tlsops
The %{name}-tlsops package implements TLS related functions to use in the
routing script, and exports pseudo variables with certificate and TLS
parameters.

%package	db_unixodbc
Summary:	OpenSIPS unixODBC Storage support
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-unixodbc < 1.6.0

%description	db_unixodbc
The %{name}-unixodbc package contains the unixODBC plugin for %{name}, which
allows a unixODBC to be used for persistent storage

%package	xcap_client
Summary:	XCAP client
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-xcap_client < 1.6.0

%description	xcap_client
The modules is an XCAP client for OpenSIPS that can be used by other modules.
It fetches XCAP elements, either documents or part of them, by sending HTTP
GET requests. It also offers support for conditional queries. It uses libcurl
library as a client-side HTTP transfer library.

%package	xmpp
Summary:	Gateway between OpenSIPS and a jabber server
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openser-xmpp < 1.6.0

%description	xmpp
This modules is a gateway between OpenSIPS and a jabber server. It enables
the exchange of instant messages between SIP clients and XMPP(jabber)
clients.

%prep
%setup -q -n %{name}-%{version}-tls
%patch0 -p0
cp -pRf modules/acc modules/acc_radius

%build
LOCALBASE=%{_prefix} CFLAGS="%{optflags}" %{make} all TLS=1 ENABLE_DIAMETER_ACC=true \
  exclude_modules="%EXCLUDE_MODULES" \
  cfg-target=%{_sysconfdir}/%{name}/ \
  modules-dir=%{_lib}/%{name}/modules

%install
rm -rf %{buildroot}
%{__make} install TLS=1 exclude_modules="%EXCLUDE_MODULES" \
  basedir=%{buildroot} prefix=%{_prefix} \
  cfg-prefix=%{buildroot} \
  modules-dir=%{_lib}/%{name}/modules
cp -pf modules/acc_radius/acc.so \
  %{buildroot}/%{_libdir}/%{name}/modules/acc_radius.so
chmod 0755 %{buildroot}/%{_libdir}/%{name}/modules/acc_radius.so

# clean some things
mkdir -p %{buildroot}/%{perl_vendorlib}
mv %{buildroot}/%{_libdir}/%{name}/perl/* \
  %{buildroot}/%{perl_vendorlib}/
mv %{buildroot}/%{_sysconfdir}/%{name}/tls/README \
  %{buildroot}/%{_docdir}/%{name}/README.tls
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL
mv %{buildroot}/%{_docdir}/%{name} docdir

# recode documentation
for i in docdir/*; do
  mv -f $i $i.old
  iconv -f iso8859-1 -t UTF-8 $i.old > $i
  rm -f $i.old
done

mkdir -p %{buildroot}%{_initrddir}
%{__install} -p -D -m 755 packaging/fedora/%{name}.init \
  %{buildroot}%{_initrddir}/%{name}
echo -e "\nETCDIR=\"%{_sysconfdir}/%{name}\"\n" \
  >> %{buildroot}%{_sysconfdir}/%{name}/%{name}ctlrc

%clean
rm -rf %{buildroot}

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files
%defattr(-,root,root,-)
%{_sbindir}/%{name}
%{_sbindir}/%{name}ctl
%{_sbindir}/%{name}dbctl
%{_sbindir}/%{name}unix
%{_sbindir}/osipsconsole

%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/tls
%dir %{_sysconfdir}/%{name}/tls/rootCA
%dir %{_sysconfdir}/%{name}/tls/rootCA/certs
%dir %{_sysconfdir}/%{name}/tls/rootCA/private
%dir %{_sysconfdir}/%{name}/tls/user
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/modules/
%dir %{_libdir}/%{name}/%{name}ctl/

%attr(755,root,root) %{_initrddir}/%{name}

%config(noreplace) %{_sysconfdir}/%{name}/dictionary.%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.cfg
%config(noreplace) %{_sysconfdir}/%{name}/%{name}ctlrc
%config(noreplace) %{_sysconfdir}/%{name}/osipsconsolerc

%config(noreplace) %{_sysconfdir}/%{name}/tls/ca.conf
%config(noreplace) %{_sysconfdir}/%{name}/tls/request.conf
%config(noreplace) %{_sysconfdir}/%{name}/tls/rootCA/cacert.pem
%config(noreplace) %{_sysconfdir}/%{name}/tls/rootCA/certs/01.pem
%config(noreplace) %{_sysconfdir}/%{name}/tls/rootCA/index.txt
%config(noreplace) %{_sysconfdir}/%{name}/tls/rootCA/private/cakey.pem
%config(noreplace) %{_sysconfdir}/%{name}/tls/rootCA/serial
%config(noreplace) %{_sysconfdir}/%{name}/tls/user.conf
%config(noreplace) %{_sysconfdir}/%{name}/tls/user/user-calist.pem
%config(noreplace) %{_sysconfdir}/%{name}/tls/user/user-cert.pem
%config(noreplace) %{_sysconfdir}/%{name}/tls/user/user-cert_req.pem
%config(noreplace) %{_sysconfdir}/%{name}/tls/user/user-privkey.pem

%{_libdir}/%{name}/%{name}ctl/%{name}ctl.*
%{_libdir}/%{name}/%{name}ctl/%{name}dbctl.base
%{_libdir}/%{name}/%{name}ctl/%{name}dbctl.dbtext
%{_libdir}/%{name}/%{name}ctl/dbtextdb/dbtextdb.py

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dbtext

%{_mandir}/man5/%{name}.cfg.5*
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}ctl.8*
%{_mandir}/man8/%{name}unix.8*

%doc docdir/AUTHORS
%doc docdir/NEWS
%doc docdir/README
%doc docdir/README-MODULES
%doc docdir/README.tls

%{_libdir}/%{name}/modules/aaa_radius.so
%{_libdir}/%{name}/modules/acc.so
%{_libdir}/%{name}/modules/alias_db.so
%{_libdir}/%{name}/modules/auth_db.so
%{_libdir}/%{name}/modules/auth.so
%{_libdir}/%{name}/modules/avpops.so
%{_libdir}/%{name}/modules/b2b_entities.so
%{_libdir}/%{name}/modules/b2b_logic.so
%{_libdir}/%{name}/modules/benchmark.so
%{_libdir}/%{name}/modules/call_control.so
%{_libdir}/%{name}/modules/cfgutils.so
%{_libdir}/%{name}/modules/closeddial.so
%{_libdir}/%{name}/modules/db_flatstore.so
%{_libdir}/%{name}/modules/db_http.so
%{_libdir}/%{name}/modules/db_http.so
%{_libdir}/%{name}/modules/db_text.so
%{_libdir}/%{name}/modules/db_virtual.so
%{_libdir}/%{name}/modules/dialog.so
%{_libdir}/%{name}/modules/dialplan.so
%{_libdir}/%{name}/modules/dispatcher.so
%{_libdir}/%{name}/modules/diversion.so
%{_libdir}/%{name}/modules/domainpolicy.so
%{_libdir}/%{name}/modules/domain.so
%{_libdir}/%{name}/modules/drouting.so
%{_libdir}/%{name}/modules/enum.so
%{_libdir}/%{name}/modules/exec.so
%{_libdir}/%{name}/modules/gflags.so
%{_libdir}/%{name}/modules/group.so
%{_libdir}/%{name}/modules/identity.so
%{_libdir}/%{name}/modules/imc.so
%{_libdir}/%{name}/modules/json.so
%{_libdir}/%{name}/modules/lcr.so
%{_libdir}/%{name}/modules/load_balancer.so
%{_libdir}/%{name}/modules/localcache.so
%{_libdir}/%{name}/modules/mangler.so
%{_libdir}/%{name}/modules/maxfwd.so
%{_libdir}/%{name}/modules/mediaproxy.so
%{_libdir}/%{name}/modules/memcached.so
%{_libdir}/%{name}/modules/mi_datagram.so
%{_libdir}/%{name}/modules/mi_fifo.so
%{_libdir}/%{name}/modules/mi_xmlrpc.so
%{_libdir}/%{name}/modules/mmgeoip.so
%{_libdir}/%{name}/modules/msilo.so
%{_libdir}/%{name}/modules/nathelper.so
%{_libdir}/%{name}/modules/nat_traversal.so
%{_libdir}/%{name}/modules/options.so
%{_libdir}/%{name}/modules/path.so
%{_libdir}/%{name}/modules/pdt.so
%{_libdir}/%{name}/modules/peering.so
%{_libdir}/%{name}/modules/permissions.so
%{_libdir}/%{name}/modules/pike.so
%{_libdir}/%{name}/modules/presence_dialoginfo.so
%{_libdir}/%{name}/modules/presence_xcapdiff.so
%{_libdir}/%{name}/modules/pua_dialoginfo.so
%{_libdir}/%{name}/modules/qos.so
%{_libdir}/%{name}/modules/ratelimit.so
%{_libdir}/%{name}/modules/regex.so
%{_libdir}/%{name}/modules/registrar.so
%{_libdir}/%{name}/modules/rr.so
%{_libdir}/%{name}/modules/signaling.so
%{_libdir}/%{name}/modules/siptrace.so
%{_libdir}/%{name}/modules/sl.so
%{_libdir}/%{name}/modules/speeddial.so
%{_libdir}/%{name}/modules/sst.so
%{_libdir}/%{name}/modules/statistics.so
%{_libdir}/%{name}/modules/stun.so
%{_libdir}/%{name}/modules/textops.so
%{_libdir}/%{name}/modules/tm.so
%{_libdir}/%{name}/modules/uac_redirect.so
%{_libdir}/%{name}/modules/uac.so
%{_libdir}/%{name}/modules/uri.so
%{_libdir}/%{name}/modules/userblacklist.so
%{_libdir}/%{name}/modules/usrloc.so
%{_libdir}/%{name}/modules/xlog.so


%doc docdir/README.acc
%doc docdir/README.alias_db
%doc docdir/README.auth
%doc docdir/README.auth_db
%doc docdir/README.avpops
%doc docdir/README.benchmark
%doc docdir/README.cfgutils
%doc docdir/README.db_text
%doc docdir/README.db_flatstore
%doc docdir/README.dialog
%doc docdir/README.dispatcher
%doc docdir/README.diversion
%doc docdir/README.domain
%doc docdir/README.domainpolicy
%doc docdir/README.enum
%doc docdir/README.exec
%doc docdir/README.gflags
%doc docdir/README.group
%doc docdir/README.imc
%doc docdir/README.lcr
%doc docdir/README.mangler
%doc docdir/README.maxfwd
%doc docdir/README.mediaproxy
%doc docdir/README.mi_fifo
%doc docdir/README.mi_datagram
%doc docdir/README.mi_xmlrpc
%doc docdir/README.msilo
%doc docdir/README.nathelper
%doc docdir/README.options
%doc docdir/README.path
%doc docdir/README.pdt
%doc docdir/README.permissions
%doc docdir/README.pike
%doc docdir/README.registrar
%doc docdir/README.rr
%doc docdir/README.siptrace
%doc docdir/README.sl
%doc docdir/README.speeddial
%doc docdir/README.sst
%doc docdir/README.statistics
%doc docdir/README.textops
%doc docdir/README.tm
%doc docdir/README.uac
%doc docdir/README.uac_redirect
%doc docdir/README.uri
%doc docdir/README.usrloc
%doc docdir/README.xlog

%files acc_radius
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/acc_radius.so
#%doc docdir/README.acc_radius

%files auth_aaa
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/auth_aaa.so
%doc docdir/README.auth_aaa

%files auth_diameter
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/auth_diameter.so
%doc docdir/README.auth_diameter

%files carrierroute
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/carrierroute.so
%doc docdir/README.carrierroute

%files cpl-c
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/cpl-c.so
%doc docdir/README.cpl-c

%files db_berkeley
%defattr(-,root,root,-)
%{_sbindir}/bdb_recover
%{_libdir}/%{name}/modules/db_berkeley.so
%{_libdir}/%{name}/%{name}ctl/%{name}dbctl.db_berkeley
%{_datadir}/%{name}/db_berkeley
%doc docdir/README.db_berkeley

%files h350
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/h350.so
%doc docdir/README.h350

%files jabber
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/jabber.so
%doc docdir/README.jabber

%files ldap
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/ldap.so
%doc docdir/README.ldap

%files db_mysql
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/db_mysql.so
%{_libdir}/%{name}/%{name}ctl/%{name}dbctl.mysql
%{_datadir}/%{name}/mysql
%doc docdir/README.db_mysql

%files perl
%defattr(-,root,root,-)
%dir %{perl_vendorlib}/OpenSIPS
%dir %{perl_vendorlib}/OpenSIPS/LDAPUtils
%dir %{perl_vendorlib}/OpenSIPS/Utils
%{_libdir}/%{name}/modules/perl.so
%{perl_vendorlib}/OpenSIPS.pm
%{perl_vendorlib}/OpenSIPS/Constants.pm
%{perl_vendorlib}/OpenSIPS/LDAPUtils/LDAPConf.pm
%{perl_vendorlib}/OpenSIPS/LDAPUtils/LDAPConnection.pm
%{perl_vendorlib}/OpenSIPS/Message.pm
%{perl_vendorlib}/OpenSIPS/Utils/PhoneNumbers.pm
%{perl_vendorlib}/OpenSIPS/Utils/Debug.pm
%doc docdir/README.perl

%files perlvdb
%defattr(-,root,root,-)
%dir %{perl_vendorlib}/OpenSIPS/VDB
%dir %{perl_vendorlib}/OpenSIPS/VDB/Adapter
%{_libdir}/%{name}/modules/perlvdb.so
%{perl_vendorlib}/OpenSIPS/VDB.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/AccountingSIPtrace.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/Alias.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/Auth.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/Describe.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/Speeddial.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/TableVersions.pm
%{perl_vendorlib}/OpenSIPS/VDB/Column.pm
%{perl_vendorlib}/OpenSIPS/VDB/Pair.pm
%{perl_vendorlib}/OpenSIPS/VDB/ReqCond.pm
%{perl_vendorlib}/OpenSIPS/VDB/Result.pm
%{perl_vendorlib}/OpenSIPS/VDB/VTab.pm
%{perl_vendorlib}/OpenSIPS/VDB/Value.pm
%doc docdir/README.perlvdb

%files db_postgres
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/db_postgres.so
%{_libdir}/%{name}/%{name}ctl/%{name}dbctl.pgsql
%{_datadir}/%{name}/postgres
%doc docdir/README.db_postgres

%files presence
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/presence.so
%doc docdir/README.presence

%files presence_mwi
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/presence_mwi.so
%doc docdir/README.presence_mwi

%files presence_xml
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/presence_xml.so
%doc docdir/README.presence_xml

%files pua
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/pua.so
%doc docdir/README.pua

%files pua_bla
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/pua_bla.so
%doc docdir/README.pua_bla

%files pua_mi
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/pua_mi.so
%doc docdir/README.pua_mi

%files pua_usrloc
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/pua_usrloc.so
%doc docdir/README.pua_usrloc

%files pua_xmpp
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/pua_xmpp.so
%doc docdir/README.pua_xmpp

%files rls
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/rls.so
%doc docdir/README.rls

%files seas
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/seas.so
%doc docdir/README.seas

%files sms
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/sms.so
%doc docdir/README.sms

%files snmpstats
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/snmpstats.so
%doc docdir/README.snmpstats
%dir %{_datadir}/snmp
%dir %{_datadir}/snmp/mibs
%{_datadir}/snmp/mibs/OPENSER-MIB
%{_datadir}/snmp/mibs/OPENSER-REG-MIB
%{_datadir}/snmp/mibs/OPENSER-SIP-COMMON-MIB
%{_datadir}/snmp/mibs/OPENSER-SIP-SERVER-MIB
%{_datadir}/snmp/mibs/OPENSER-TC

%files tlsops
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/tlsops.so
%doc docdir/README.tlsops

%files db_unixodbc
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/db_unixodbc.so
%doc docdir/README.db_unixodbc

%files xcap_client
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/xcap_client.so
%doc docdir/README.xcap_client

%files xmpp
%defattr(-,root,root,-)
%{_libdir}/%{name}/modules/xmpp.so
%doc docdir/README.xmpp

