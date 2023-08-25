#!/bin/bash
#run cmd : source common.sh , then run test

function test(){
  echo "test"
}

function sleep10(){
  sleep 60
}

function shutdown(){
  ps -ef |grep auto | grep -v grep | awk '{print $2}'|xargs kill -9

}