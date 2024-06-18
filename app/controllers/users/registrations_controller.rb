class Users::RegistrationsController < Devise::RegistrationsController
  before_action :configure_permitted_parameters, if: :devise_controller?

  protected

  def configure_permitted_parameters
    devise_parameter_sanitizer.permit(:sign_up, keys: [:full_name, :description, :image, :role])
    devise_parameter_sanitizer.permit(:account_update, keys: [:full_name, :description, :image, :role])
  end
end
