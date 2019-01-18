#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative 'extract_yaml'

extract_yaml 'competitions', flatten: true do |id, content|
  content['competitions']&.slice('hardwareApiCompetition', 'themedCompetition')&.values
end
