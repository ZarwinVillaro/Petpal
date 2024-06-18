class InboxController < ApplicationController
  def index
    @adoptions = Adoption.all
  end
end
