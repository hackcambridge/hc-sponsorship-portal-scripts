#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative 'extract_yaml'

extract_yaml 'tech', flatten: true do |id, content|
  content['tech']&.collect { |item| item.slice('description', 'link', 'name') }
end
