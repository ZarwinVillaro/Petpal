class ResourcesUsersideController < ApplicationController
  def tips
    @resources = Resource.all
  end
end
