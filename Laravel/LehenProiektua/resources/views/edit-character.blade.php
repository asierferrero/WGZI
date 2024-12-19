@extends('layouts.app')

@section('content')
<div class="container">
    <h1>{{ __('messages.edit_character') }}</h1><br>
    <form action="{{ route('update', ['id' => $character->id]) }}" method="POST">
        @csrf
        <div class="form-group">
            <label for="name">{{ __('messages.name') }}</label>
            <input type="text" class="form-control" id="name" name="name" value="{{ $character->name }}" required>
        </div><br>
        <div class="form-group">
            <label for="actor">{{ __('messages.actor') }}</label>
            <input type="text" class="form-control" id="actor" name="actor" value="{{ $character->actor }}" required>
        </div><br>
        <button type="submit" class="btn btn-success">{{ __('messages.submit') }}</button>
    </form>
</div>
@endsection