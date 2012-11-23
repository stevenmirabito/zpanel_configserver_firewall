#!/usr/bin/perl
#WHMADDON:addonupdates:ConfigServer Security&<b>Firewall</b>
###############################################################################
# Copyright 2006-2012, Way to the Web Limited
# URL: http://www.configserver.com
# Email: sales@waytotheweb.com
###############################################################################
# start main

use File::Find;
use Fcntl qw(:DEFAULT :flock);
use Sys::Hostname qw(hostname);
use IPC::Open3;

open (IN, "</etc/csf/version.txt") or die $!;
$myv = <IN>;
close (IN);
chomp $myv;

$script = "/modules/csf/cgi-bin/index.cgi";
$images = "/modules/csf/assets/images";

my $buffer = $ENV{'QUERY_STRING'};
if ($buffer eq "") {$buffer = $ENV{POST}}
my @pairs = split(/&/, $buffer);
foreach my $pair (@pairs) {
	my ($name, $value) = split(/=/, $pair);
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$FORM{$name} = $value;
}

header("ConfigServer Security & Firewall",,,,,,,"");

print "<img src='images/csf_small.png' align='absmiddle' /> <b style='font-size: 14px'>ConfigServer Security & Firewall - csf v$myv</b>";

do "/etc/csf/csfui.pl";

1;
