<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Character;

class ApiController extends Controller
{
    public function show()
    {
        return response()->json(Character::all());
    }

    public function showById($id)
    {
        $character = Character::findOrFail($id);
        return response()->json($character);
    }
    
    public function post(Request $request)
    {
        $character = new Character;
        $character->actor = $request->actor;
        $character->name = $request->name;
        $character->description = $request->description;
        $character->house_id = $request->house_id;
        $character->save();
        return response()->json($character);
    }

    public function update(Request $request, $id)
    {
        $character = Character::findOrFail($id);
        $character->actor = $request->actor;
        $character->name = $request->name;
        $character->description = $request->description;
        $character->house_id = $request->house_id;
        $character->save();
        return response()->json($character);
    }

    public function delete($id)
    {
        $character = Character::findOrFail($id);
        $character->delete();
        return response()->json(['message' => 'Character deleted successfully']);
    }
}
