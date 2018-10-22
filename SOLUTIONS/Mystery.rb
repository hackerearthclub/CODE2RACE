#!/usr/bin/ruby
#coding:utf-8
#author:cielavenir (https://github.com/cielavenir)

require 'prime'
gets.to_i.times{
	p gets.to_i.prime_division.map{|n,p|p+1}.reduce 1,:*
}
