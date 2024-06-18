class AdoptPetsController < ApplicationController
  def index
    if current_user && current_user.role == "pet_owner"
      @pets = current_user.pets
    else
      @pet_owners = User.where(role: 'pet_owner')
    end
  end


  def view_pet
    @pet_owner = User.find(params[:pet_owner_id])
    @pets = @pet_owner.pets

    if params[:category].present? && params[:category] != 'all'
      @pets = @pets.where(category: params[:category])
    end
  end



  def pets_category
    @pet_owner = User.find(params[:pet_owner_id])
    @pets = @pet_owner.pets

    if params[:category].present? && params[:category] != 'all'
      @pets = @pets.where(category: params[:category])
    end

    render :view_pet
  end



  
  def adoptation_form
    @adoption = Adoption.new
  end

  def create_adoption
    @adoption = Adoption.new(adoption_params)
    if @adoption.save
      # Redirect to a success page or display a success message
      redirect_to root_path, notice: "Adoption request submitted successfully!"
    else
      # If the form doesn't save, render the form again with error messages
      render :adoptation_form
    end
  end

  private

  def adoption_params
    params.require(:adoption).permit(:full_name, :address, :contact, :reason, :user_id, :pet_id)
  end
end