using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using IdentityManager.Data;
using IdentityManager.Models;

namespace IdentityManager.Controllers;

[ApiController]
[Route("api/[controller]")]
public class RolesController : ControllerBase
{
    private readonly AppDbContext _context;

    public RolesController(AppDbContext context)
    {
        _context = context;
    }

    [HttpGet]
    public async Task<ActionResult<IEnumerable<Role>>> GetRoles()
    {
        return await _context.Roles.Include(r => r.Entitlements).ToListAsync();
    }

    [HttpGet("entitlements")]
    public async Task<ActionResult<IEnumerable<Entitlement>>> GetEntitlements()
    {
        return await _context.Entitlements.ToListAsync();
    }
}
