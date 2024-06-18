Rails.application.routes.draw do
  get 'inbox/index'
  get 'resources_userside/tips'
  resources :resources
  resources :adoptions

  get 'adopt_pets/index'
  get 'adopt_pets/adoptation_form'
  get 'adopt_pets/view_pet'
  get 'adopt_pets/pets_category/:pet_owner_id', to: 'adopt_pets#pets_category', as: 'pets_category'
  post 'adopt_pets/create_adoption', to: 'adopt_pets#create_adoption', as: 'create_adoption'


  resources :adopt_pets do
    collection do
      get 'view_pet/:pet_owner_id', to: 'adopt_pets#view_pet', as: 'view_pet'
    end
  end

  resources :pets do
    collection do
      get 'adopt', to: 'pets#index', as: 'adopt_pets'
    end
  end

  root 'pages#home'

  devise_for :users, controllers: {
    registrations: 'users/registrations'
  }

  get "up" => "rails/health#show", as: :rails_health_check
end
