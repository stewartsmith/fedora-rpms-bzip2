# Makefile for source rpm: bzip2
# $Id$
NAME := bzip2
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
