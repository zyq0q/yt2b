#!/bin/bash

function sleep10(){
  sleep 10
}

function shutdown(){
  ps -ef |grep auto | grep -v grep | awk '{print $2}'|xargs kill -9

}