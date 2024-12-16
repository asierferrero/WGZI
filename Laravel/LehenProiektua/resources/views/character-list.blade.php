@extends('layouts.app')
@php
    use Illuminate\Support\Facades\Auth;
@endphp
@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-10 col-md-offset-1">
            <h1 class="panel panel-success">
                <h1>{{ __('messages.title') }}</h1><br>
                @if(Auth::check())
                    <!-- Table -->
                    <table class="table">
                        <tr>
                            <th>{{ __('messages.name') }}</th>
                            <th>{{ __('messages.actor') }}</th>
                            <th></th>
                        </tr>
                        @foreach($characters as $character)
                            <tr>
                                <td>{{ $character->name }}</td>
                                <td>{{ $character->actor }}</td>
                                <td><a href="{{ route('delete', ['id' => $character->id]) }}" class="btn">🗑️</a></td>
                            </tr>
                        @endforeach
                    </table>
                    <br><a href="/form" class="btn btn-success">{{ __('messages.new') }}</a>
                @endif
                @if(Auth::guest())
                    <a href="/login" class="btn btn-info">{{ __('messages.login') }}</a>
                @endif
        </div><br>
    </div>
</div>
</div>
@endsection