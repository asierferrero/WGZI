@extends('layouts.app')
@section('content')
<div class="container">
    <div class="row">
        <h1>{{ __('messages.title2') }}</h1>
        <form action="/submit" method="post"><br>
            @if ($errors->any())
                <div class="alert alert-danger" role="alert">{{ __('messages.errors') }}</div>
            @endif
            {!! csrf_field() !!}
            <div class="form-group{{ $errors->has('name') ? ' has-error' :
    '' }}">
                <label for="name">{{ __('messages.character_name') }}</label>
                <input type="text" class="form-control" id="name" name="name" placeholder="{{ __('messages.name') }}"
                    value="{{ old('name') }}">
                @if($errors->has('name'))
                    <span class="help-block">{{ $errors->first('name') }}
                    </span>
                @endif
            </div><br>
            <div class="form-group{{ $errors->has('actor') ? ' has-error' :
    '' }}">
                <label for="actor">{{ __('messages.actor') }}</label>
                <input type="text" class="form-control" id="actor" name="actor" placeholder="{{ __('messages.actor') }}"
                    value="{{ old('actor') }}">
                @if($errors->has('actor'))
                    <span class="help-block">{{ $errors->first('actor') }}
                    </span>
                @endif
            </div><br>
            <div class="form-group{{ $errors->has('description') ? ' haserror' : '' }}">
                <label for="description">{{ __('messages.description') }}</label>
                <textarea class="form-control" id="description" name="description"
                    placeholder="{{ __('messages.description') }}">{{ old('description')
}}</textarea>
                @if($errors->has('description'))
                    <span class="help-block">{{ $errors->first('description') }}</span>
                @endif
            </div><br>
            <div class="form-group{{ $errors->has('house_id') ? ' has-error' : '' }}">
                <label for="house_id">{{ __('messages.house') }}</label>
                <select class="form-control" id="house_id" name="house_id">
                    @foreach($houses as $house)
                        <option value="{{$house->id}}">{{$house->name}}</option>
                    @endforeach
                </select>
                @if($errors->has('description'))
                    <span class="help-block">{{ $errors->first('description') }}</span>
                @endif
            </div><br>
            <button type="submit" class="btn btn-success">{{ __('messages.submit') }}</button>
            <a href="/" class="btn btn-danger mx-2">{{ __('messages.return') }}</a>
        </form>
    </div>
</div>
@endsection