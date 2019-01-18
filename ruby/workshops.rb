#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative 'extract_yaml'

extract_yaml 'workshops' { |id, content| content['workshop']&.slice('description', 'title') }
