class PagesController < ApplicationController
  def home
    if current_user && current_user.role == "pet_owner"
      @pets = current_user.pets
    else
      @pet_owners = User.where(role: 'pet_owner')
    end
  end
end
