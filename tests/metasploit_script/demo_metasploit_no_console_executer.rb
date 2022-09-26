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
  
  require Pathname.new(metasploit_msfconsole_location).realpath.expand_path.parent.join('config', 'boot')
  require 'msfenv'
  require 'metasploit/framework/profiler'
  require 'metasploit/framework/command/console'

  Metasploit::Framework::Profiler.start
#   Metasploit::Framework::Command::Console.start
rescue Interrupt
  puts "\nAborting..."
  exit(1)
end