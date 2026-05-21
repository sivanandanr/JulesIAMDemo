using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using IdentityManager.Data;
using IdentityManager.Models;

namespace IdentityManager.Controllers;

[ApiController]
[Route("api/[controller]")]
public class ConnectorsController : ControllerBase
{
    private readonly AppDbContext _context;

    public ConnectorsController(AppDbContext context)
    {
        _context = context;
    }

    [HttpGet]
    public async Task<ActionResult<IEnumerable<Connector>>> GetConnectors()
    {
        return await _context.Connectors.Include(c => c.Applications).ToListAsync();
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<Connector>> GetConnector(int id)
    {
        var connector = await _context.Connectors
            .Include(c => c.Applications)
            .FirstOrDefaultAsync(c => c.Id == id);

        if (connector == null) return NotFound();
        return connector;
    }

    [HttpPut("{id}/provisioning")]
    public async Task<IActionResult> UpdateProvisioning(int id, [FromBody] string config)
    {
        var connector = await _context.Connectors.FindAsync(id);
        if (connector == null) return NotFound();

        connector.ProvisioningConfig = config;
        await _context.SaveChangesAsync();

        return NoContent();
    }
}
