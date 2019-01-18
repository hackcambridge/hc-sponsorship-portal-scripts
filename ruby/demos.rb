#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative 'extract_yaml'

extract_yaml 'demos' { |id, content| content['demo']&.slice('description', 'title') }
