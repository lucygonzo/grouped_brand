// Grouped Design System — Figma Variable Updater
// Paste this entire script into Figma Dev Console:
// Menu → Plugins → Development → Open Console
//
// This updates all mismatched variables to match the brand guide.
// Run in your GDS26R Lucy Test file.

(async () => {
  const collections = await figma.variables.getLocalVariableCollectionsAsync();
  const allVars = await figma.variables.getLocalVariablesAsync();

  // Build a lookup by variable name
  const varMap = {};
  for (const v of allVars) {
    varMap[v.name] = v;
  }

  const log = [];
  const errors = [];

  // Helper: update a variable's value across all modes
  function updateVar(name, newValue) {
    const v = varMap[name];
    if (!v) {
      errors.push(`Variable "${name}" not found`);
      return;
    }
    // Get the collection to find modes
    const collection = collections.find(c => c.id === v.variableCollectionId);
    if (!collection) {
      errors.push(`Collection not found for "${name}"`);
      return;
    }
    for (const mode of collection.modes) {
      const oldValue = v.valuesByMode[mode.modeId];
      v.setValueForMode(mode.modeId, newValue);
      log.push(`✓ ${name}: ${oldValue} → ${newValue} (mode: ${mode.name})`);
    }
  }

  // =========================================
  // TASK 1: Fix D0 variable values
  // =========================================
  updateVar("font/size/6xl", 96);           // was 64
  updateVar("font/line-height/6xl", 116);   // was 72

  // =========================================
  // TASK 4: Ensure weight variables exist
  // (Bold=700, Medium=500, Regular=400)
  // These should already be correct but verify
  // =========================================
  // updateVar("font/weight/Bold", 700);
  // updateVar("font/weight/Medium", 500);
  // updateVar("font/weight/Regular", 400);

  // =========================================
  // Check if font/line-height/xl (28px) exists
  // If not, create it — needed for H4
  // =========================================
  if (!varMap["font/line-height/xl"]) {
    // Find the collection that holds line-height vars
    const lhVar = varMap["font/line-height/lg"];
    if (lhVar) {
      const collection = collections.find(c => c.id === lhVar.variableCollectionId);
      if (collection) {
        const newVar = figma.variables.createVariable("font/line-height/xl", collection.id, "FLOAT");
        for (const mode of collection.modes) {
          newVar.setValueForMode(mode.modeId, 28);
        }
        log.push("✓ Created font/line-height/xl = 28 (new variable)");
        varMap["font/line-height/xl"] = newVar;
      }
    }
  } else {
    // Verify it's 28
    updateVar("font/line-height/xl", 28);
  }

  // =========================================
  // Print results
  // =========================================
  console.log("\n=== GROUPED TOKEN UPDATER ===\n");

  if (log.length > 0) {
    console.log("UPDATED:");
    log.forEach(l => console.log("  " + l));
  }

  if (errors.length > 0) {
    console.log("\nERRORS:");
    errors.forEach(e => console.log("  ✗ " + e));
  }

  console.log(`\nDone: ${log.length} updates, ${errors.length} errors`);

  // =========================================
  // MANUAL STEPS STILL NEEDED
  // (Can't be done via variables API)
  // =========================================
  console.log("\n=== MANUAL STEPS REMAINING ===");
  console.log("These require editing text styles or layers directly:\n");
  console.log("TASK 2 — Rebind line-height variables on text layers:");
  console.log("  D6: rebind line-height sm → md");
  console.log("  H4: rebind line-height lg → xl (28px, just created above)");
  console.log("  H5: rebind line-height md → lg");
  console.log("  Caption: rebind line-height sm → md");
  console.log("  C6: rebind line-height xs → sm");
  console.log("");
  console.log("TASK 3 — Letter-spacing (set on text layers):");
  console.log("  D0 (node 757:1295): set letter-spacing to -4%");
  console.log("  D1 (node 729:396): set letter-spacing to -3%");
  console.log("");
  console.log("TASK 4 — Font weights (set on text layers):");
  console.log("  D0, D1, C1-C4: set to Bold 700");
  console.log("  D4: set to Medium 500");
  console.log("");
  console.log("TASK 5 — Rename text styles:");
  console.log('  "Fine Print" → "Caption"');
  console.log('  "Fine Print Emphasized" → "Caption Emphasized"');
  console.log("");
  console.log("TASK 6 — Global cleanup:");
  console.log("  Replace all Inter → Satoshi");
  console.log("  Replace all #f8f8f8 → #F0EBE3");
  console.log("");
  console.log("TASK 7 — Nav menu color remap:");
  console.log("  Nav-menu #f8f8f8 → Text/Core/Primary #F0EBE3");
  console.log("  Nav-menu-secondary #d2d3d6 → Text/Core/Muted #A09B93");
  console.log("  color/blue/400 #4f96d0 → Brand/Focus Blue #7CBBDF");
  console.log("  Menu Link Active #101323 → Fill/Core/Base #111620");
  console.log("  Fill/Interactive/Nav-menu #181e2a → Fill/Core/L1 #181E2A");
})();
