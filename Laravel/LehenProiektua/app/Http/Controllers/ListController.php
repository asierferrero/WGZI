<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ListController extends Controller
{
    public function show()
    {
        $characters = \App\Models\Character::all();
        return view('character-list', ['characters' => $characters]);
    }

    public function showFiltered(Request $request)
    {
        $query = \App\Models\Character::where('name', $request->query('name'));
        $characters = $query->get();
        return view('character-list', ['characters' => $characters]);
    }

    public function delete($id)
    {
        $character = \App\Models\Character::find($id);

        if ($character) {
            $character->delete();
            return redirect('/');
        } else {
            return redirect('/');
        }
    }

    public function edit($id)
    {
        $character = \App\Models\Character::find($id);

        if ($character) {
            return view('edit-character', compact('character'));
        } else {
            return redirect('/');
        }
    }

    public function update(Request $request, $id)
    {
        $character = \App\Models\Character::find($id);

        if ($character) {
            $character->name = $request->input('name');
            $character->actor = $request->input('actor');
            $character->save();
            return redirect('/');
        } else {
            return redirect('/');
        }
    }
}