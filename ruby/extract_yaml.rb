# frozen_string_literal: true

require 'json'
require 'yaml'
require 'firebase'

def extract_yaml(name, options = {})
  private_key = File.open(ARGV[0]).read
  firebase = Firebase::Client.new('https://hack-cambridge-sponsors-portal.firebaseio.com/', private_key)
  data = firebase.get('sponsors').body.collect { |id, content| yield(id, content) }.compact
  data.flatten! if options[:flatten]
  File.new("#{name}-#{Time.now.strftime('%Y%m%d%H%M%S')}.yml", 'w')&.syswrite(data.to_yaml)
end
