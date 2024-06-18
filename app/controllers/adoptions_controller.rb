class AdoptionsController < ApplicationController
    def index
        @adoptions = Adoption.all
      end

        def destroy
        @adoption = Adoption.find(params[:id])
        @adoption.destroy
        redirect_to adoptions_path, notice: 'Adoption was successfully deleted.'
        end
  
    private
  
    def adoption_params
      params.require(:adoption).permit(:full_name, :address, :contact, :reason, :user_id, :pet_id)
    end
  end
  