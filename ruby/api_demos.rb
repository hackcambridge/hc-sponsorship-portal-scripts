#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative 'extract_yaml'

def extract_api_demos
  extract_yaml 'api_demos' do |id, content|
    content['demo']&.slice('description', 'title')
  end
end
