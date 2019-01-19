#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative 'extract_yaml'

def extract_prizes
  extract_yaml 'prizes', flatten: true do |id, content|
    content['competitions']&.slice('hardwareApiCompetition', 'themedCompetition')&.values
  end
end
