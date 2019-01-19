#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative 'extract_yaml'

def extract_workshops
  extract_yaml 'workshops' do |id, content|
    content['workshop']&.slice('description', 'title')
  end
end
