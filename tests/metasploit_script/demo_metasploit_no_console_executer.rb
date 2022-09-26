#!/usr/share/metasploit-framework/ruby
# -*- coding: binary -*-
#
# This user interface provides users with a command console interface to the
# framework.
#

require 'pathname'
begin

  # Silences warnings as they only serve to confuse end users
  if defined?(Warning) && Warning.respond_to?(:[]=)
    Warning[:deprecated] = false
  end

  # @see https://github.com/rails/rails/blob/v3.2.17/railties/lib/rails/generators/rails/app/templates/script/rails#L3-L5
  ## this is probably not the file path.
  metasploit_msfconsole_location = "/usr/bin/msfconsole"
  # what the heck is going on?
  require Pathname.new(metasploit_msfconsole_location).realpath.expand_path.parent.join('config', 'boot')
  require 'msfenv'
  require 'metasploit/framework/profiler'
  require 'metasploit/framework/command/console'

  Metasploit::Framework::Profiler.start
#   Metasploit::Framework::Command::Console.start
print("load complete\n")
search_string = Msf::Modules::Metadata::Search.parse_search_string("cve:2008")

result = Msf::Modules::Metadata::Cache.instance.find(search_string)

$LOAD_PATH << "/var/lib/gems/3.0.0/gems/awesome_print-1.9.2/lib/"
# $LOAD_PATH << "/var/lib/gems/3.0.0/gems/amazing_print-1.4.0/lib/"
# require '/var/lib/gems/3.0.0/gems/amazing_print-1.4.0'
# use the gem inside the msfconsole.
# maybe not.
# require 'amazing_print'
require 'ap'
# how about let's use absolute import path?
# print(result)
# puts(result)
# ap result


ANSI_BOLD       = "\033[1m"
ANSI_RESET      = "\033[0m"
ANSI_LGRAY    = "\033[0;37m"
ANSI_GRAY     = "\033[1;30m"

def pm(obj, *options) # Print methods
  methods = obj.methods
  methods -= Object.methods unless options.include? :more
  filter = options.select {|opt| opt.kind_of? Regexp}.first
  methods = methods.select {|name| name =~ filter} if filter

  data = methods.sort.collect do |name|
    method = obj.method(name)
    if method.arity == 0
      args = "()"
    elsif method.arity > 0
      n = method.arity
      args = "(#{(1..n).collect {|i| "arg#{i}"}.join(", ")})"
    elsif method.arity < 0
      n = -method.arity
      args = "(#{(1..n).collect {|i| "arg#{i}"}.join(", ")}, ...)"
    end
    klass = $1 if method.inspect =~ /Method: (.*?)#/
    [name, args, klass]
  end
  max_name = data.collect {|item| item[0].size}.max
  max_args = data.collect {|item| item[1].size}.max
  data.each do |item| 
    print " #{ANSI_BOLD}#{item[0].rjust(max_name)}#{ANSI_RESET}"
    print "#{ANSI_GRAY}#{item[1].ljust(max_args)}#{ANSI_RESET}"
    print "   #{ANSI_LGRAY}#{item[2]}#{ANSI_RESET}\n"
  end
  data.size
end

# data = [ false, 42, %w(forty two), { :now => Time.now, :class => Time.now.class, :distance => 42e42 } ]
# ap data
pm r
# how to pretty print?
# gem install amazing_print
$LOAD_PATH << "." # must add this line
require 'test'

rescue Interrupt
  puts "\nAborting..."
  exit(1)
end